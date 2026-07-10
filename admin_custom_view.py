from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from public.util.rsa_utils import decrypt_password, get_public_key


class CustomRsaAdminLoginView(LoginView):
    # 强制指定admin登录模板路径，解决找不到registration/login.html报错
    template_name = "admin/login.html"

    # 关键修复：设置默认跳转地址，取不到next时用admin首页
    success_url = reverse_lazy('admin:index')

    def get_context_data(self, **kwargs):
        # 把RSA公钥传给前端模板
        ctx = super().get_context_data(**kwargs)
        ctx["rsa_public_key"] = get_public_key()
        return ctx

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username", "").strip()
        enc_pwd = request.POST.get("password", "").strip()

        try:
            # RSA解密得到原始明文密码
            raw_password = decrypt_password(enc_pwd)
        except Exception as e:
            messages.error(request, "密码解密失败，请刷新重试")
            return super().get(request)

        # 使用原生Django校验用户（数据库仍PBKDF2加密存储）
        user = authenticate(request, username=username, password=raw_password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next", self.success_url)
            return HttpResponseRedirect(next_url)
        messages.error(request, "用户名或密码错误")
        return super().get(request)
