#!/usr/bin/env python

import json
import jwt
import datetime

def encode_jwt_RS256(body, put_iat_exp, exp_delta, private_key_file_name):
    payload = json.loads(body)
    if put_iat_exp:
        payload['iat'] = datetime.datetime.utcnow()
        payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=exp_delta)
    private_key = open(private_key_file_name,"rb").read()
    return jwt.encode(payload, private_key, algorithm='RS256')

def decode_jwt_RS256(token, public_key_file_name):
    public_key = open(public_key_file_name,"rb").read()
    body = jwt.decode(token, public_key, algorithms='RS256')
    return json.dumps(body, indent=4)

def decode_Jwt_RS256_no_validation(token, public_key_file_name):
    public_key = open(public_key_file_name,"rb").read()
    body = jwt.decode(token, public_key, algorithms='RS256', verify=False)
    return json.dumps(body, indent=4)

#def test():
#    body = "{\n  \"sub\": \"1234567890\",\n  \"name\": \"John Doe\",\n  \"admin\": true,\n  \"iat\": 1516239022,\n  \"exp\": 1516242622\n}"
#    payload = json.loads(body)
#    payload['iat'] = datetime.datetime.utcnow()
#    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
#    print(payload)
#    private_key = open("private.rsa256.key","rb").read()
#    public_key = open("public.rsa256.key","rb").read()
#    encoded = jwt.encode(payload, private_key, algorithm='RS256')
#    print(encoded)
#    def decode_jwt():
#        try:
#            return jwt.decode(encoded, public_key, algorithms='RS256')
#        except jwt.ExpiredSignatureError:
#            print("Signature expired")
#            return None
#    decoded = jwt.decode(encoded, public_key, algorithms='RS256')
#    print(decoded)
#
#
#import wx
#import sys
#import traceback
#import lib_jwt_generator as jwt
#
#  def on_open_private_key_file(self, event):  # wxGlade: MainFrame.<event_handler>
#    print("Event handler 'on_open_private_key_file' not implemented!")
#    event.Skip()
#
#  def on_open_public_key_file(self, event):  # wxGlade: MainFrame.<event_handler>
#    print("Event handler 'on_open_public_key_file' not implemented!")
#    event.Skip()
#
#  def on_generate_jwt_token(self, event):  # wxGlade: MainFrame.<event_handler>
#    body = self.text_ctrl_1.GetValue()
#    put_iat_exp = self.checkbox_1.GetValue()
#    exp_delta = self.spin_ctrl_1.GetValue()
#    private_key_file_name = self.text_ctrl_2.GetValue()
#    encoded = jwt.encode_jwt_RS256(body, put_iat_exp, exp_delta, private_key_file_name)
#    self.text_ctrl_4.SetValue(encoded)
#    event.Skip()
#
#  def on_copy_token(self, event):  # wxGlade: MainFrame.<event_handler>
#    token = self.text_ctrl_4.GetValue()
#    if wx.TheClipboard.Open():
#        wx.TheClipboard.SetData(wx.TextDataObject(token))
#        wx.TheClipboard.Close()
#    event.Skip()
#
#  def on_exit(self, event):  # wxGlade: MainFrame.<event_handler>
#    self.Close()
#
# end of class MainFrame
#
#class ExceptionDialog():
#
#    def __init__(self, msg):
#        wx.MessageBox(msg, 'Error!', wx.OK | wx.ICON_ERROR)
#
# end of class ExceptionDialog
#
#def MyExceptionHook(etype, value, trace):
#    """
#    https://www.blog.pythonlibrary.org/2014/01/31/wxpython-how-to-catch-all-exceptions/
#    Handler for all unhandled exceptions.
#    :param `etype`: the exception type (`SyntaxError`, `ZeroDivisionError`, etc...);
#    :type `etype`: `Exception`
#    :param string `value`: the exception error message;
#    :param string `trace`: the traceback header, if any (otherwise, it prints the
#     standard Python header: ``Traceback (most recent call last)``.
#    """
#    frame = wx.GetApp().GetTopWindow()
#    tmp = traceback.format_exception(etype, value, trace)
#    exception = "".join(tmp)
#    dlg = ExceptionDialog(exception)
#    dlg.ShowModal()
#    dlg.Destroy()
#
# end of function MyExceptionHook
#
#class JwtGenerator(wx.App):
#  def OnInit(self):
#    self.frame = MainFrame(None, wx.ID_ANY, "")
#    sys.excepthook = MyExceptionHook
#    self.SetTopWindow(self.frame)
#    self.frame.Show()
#    return True
#
