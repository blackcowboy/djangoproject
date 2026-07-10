from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
import os
from django.conf import settings

# 密钥存放路径
KEY_DIR = os.path.join(settings.BASE_DIR, "rsa_keys")
PRIVATE_KEY_PATH = os.path.join(KEY_DIR, "private.key")
PUBLIC_KEY_PATH = os.path.join(KEY_DIR, "public.key")

# 自动创建密钥文件夹
if not os.path.exists(KEY_DIR):
    os.makedirs(KEY_DIR)


def generate_rsa_key(bits=2048):
    """生成 RSA 公私钥对"""
    key = RSA.generate(bits)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open(PRIVATE_KEY_PATH, "wb") as f:
        f.write(private_key)

    with open(PUBLIC_KEY_PATH, "wb") as f:
        f.write(public_key)
    return private_key, public_key


def get_public_key():
    """读取公钥，返回字符串给前端"""
    if not os.path.exists(PUBLIC_KEY_PATH):
        generate_rsa_key()
    with open(PUBLIC_KEY_PATH, "r", encoding="utf-8") as f:
        return f.read()


def decrypt_password(encrypted_base64: str) -> str:
    """后端用私钥解密前端传过来的base64密文密码"""
    with open(PRIVATE_KEY_PATH, "r", encoding="utf-8") as f:
        private_key = RSA.import_key(f.read())

    cipher = PKCS1_v1_5.new(private_key)
    encrypted_data = base64.b64decode(encrypted_base64)
    raw_pwd_bytes = cipher.decrypt(encrypted_data, sentinel=None)
    if raw_pwd_bytes is None:
        raise ValueError("密码解密失败")
    return raw_pwd_bytes.decode("utf-8")

