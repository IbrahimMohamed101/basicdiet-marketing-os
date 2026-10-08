import io
import json
import os
import unittest
import urllib.error
from unittest.mock import MagicMock, patch
from scripts import daily_brief as d
from scripts import provider as p


class ProviderTests(unittest.TestCase):
    def setUp(self):
        self.packet=d.make_packet(d.load_ideas(d.IDEAS)[2],'instagram','2026-10-08',0)
        self.packet['sources']=[{'secret':'DO_NOT_SEND_SOURCE'}]

    def respond(self,raw):
        opener=MagicMock()
        opener.open.return_value.__enter__.return_value.read.return_value=raw
        return opener

    def test_key_required_no_network(self):
        with patch.dict(os.environ,{},clear=True),patch.object(p.urllib.request,'build_opener') as net:
            with self.assertRaisesRegex(ValueError,'OPENAI_API_KEY'):p.ai_suggestions(self.packet,'gpt-5')
            net.assert_not_called()

    def test_payload_bounded_allowlisted_no_storage_and_one_request(self):
        opener=self.respond(json.dumps({'status':'completed','output':[{'type':'message','content':[{'type':'output_text','text':'مسودة'}]}]}).encode())
        with patch.dict(os.environ,{'OPENAI_API_KEY':'test-secret'}),patch.object(p.urllib.request,'build_opener',return_value=opener):
            text=p.ai_suggestions(self.packet,'gpt-5',800)
        self.assertIn('UNVERIFIED',text)
        opener.open.assert_called_once()
        request=opener.open.call_args.args[0]
        payload=json.loads(request.data)
        self.assertFalse(payload['store'])
        self.assertEqual(payload['max_output_tokens'],800)
        self.assertNotIn('tools',payload)
        self.assertNotIn('DO_NOT_SEND_SOURCE',request.data.decode())
        self.assertNotIn('catalog',request.data.decode())
        self.assertEqual(opener.open.call_args.kwargs['timeout'],30)

    def test_malformed_empty_incomplete_and_oversized_responses(self):
        cases=[b'{',b'[]',b'{"status":"incomplete","output":[]}',b'{"status":"completed","output":[]}',
               b'{"status":"completed","output":[null]}',b'{"status":"completed","output":"bad"}',b'x'*(p.MAX_RESPONSE_BYTES+1)]
        for raw in cases:
            with self.subTest(raw=raw[:40]),patch.dict(os.environ,{'OPENAI_API_KEY':'test-secret'}),patch.object(p.urllib.request,'build_opener',return_value=self.respond(raw)):
                with self.assertRaises(ValueError):p.ai_suggestions(self.packet,'gpt-5')

    def test_http_timeout_errors_never_log_bodies_or_retry(self):
        errors=[urllib.error.HTTPError('https://api.openai.com',429,'private provider body',{},io.BytesIO(b'SECRET')),
                urllib.error.URLError('SECRET'),TimeoutError('SECRET')]
        for error in errors:
            opener=MagicMock();opener.open.side_effect=error
            with self.subTest(error=type(error)),patch.dict(os.environ,{'OPENAI_API_KEY':'test-secret'}),patch.object(p.urllib.request,'build_opener',return_value=opener):
                with self.assertRaises(ValueError) as exc:p.ai_suggestions(self.packet,'gpt-5')
            self.assertNotIn('SECRET',str(exc.exception));opener.open.assert_called_once()

    def test_config_and_input_limits_prevent_network(self):
        with patch.dict(os.environ,{'OPENAI_API_KEY':'test-secret'}),patch.object(p.urllib.request,'build_opener') as net:
            for model,tokens in [('bad/model',1200),('gpt-5',0),('gpt-5',2001)]:
                with self.assertRaises(ValueError):p.ai_suggestions(self.packet,model,tokens)
            self.packet['creative']['caption_draft']='x'*20000
            with self.assertRaisesRegex(ValueError,'input exceeds'):p.ai_suggestions(self.packet,'gpt-5')
            net.assert_not_called()

    def test_redirect_cannot_forward_credentials(self):
        with self.assertRaisesRegex(ValueError,'redirect refused'):
            p.NoRedirect().redirect_request(None,None,302,'',{},'https://other.example')
