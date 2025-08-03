import hashlib
import time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

# 模块一：区块链基础
# 实战 1：编码模拟工作量证明（POW）过程与非对称加密应用


def generate_rsa_keys():
    """生成RSA公私钥对"""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


def mine(nickname, difficulty):
    """执行POW挖矿，直到找到满足难度要求的哈希值"""
    target = '0' * difficulty
    nonce = 0
    start_time = time.time()
    
    while True:
        # 构建要哈希的内容
        content = f"{nickname}{nonce}"
        # 计算SHA256哈希
        hash_result = hashlib.sha256(content.encode()).hexdigest()
        
        # 检查是否满足难度要求
        if hash_result.startswith(target):
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"找到满足难度要求的哈希值! 耗时: {elapsed_time:.4f}秒")
            print(f"内容: {content}")
            print(f"哈希值: {hash_result}")
            print(f"nonce: {nonce}")
            return content, hash_result, elapsed_time
        
        nonce += 1


def sign_with_private_key(private_key, data):
    """使用私钥对数据进行签名"""
    signature = private_key.sign(
        data.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


def verify_with_public_key(public_key, data, signature):
    """使用公钥验证签名"""
    try:
        public_key.verify(
            signature,
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False


def main():
    # 1. 生成RSA公私钥对
    print("1. 生成RSA公私钥对...")
    private_key, public_key = generate_rsa_keys()
    print("   公私钥对生成完成!")
    
    # 2. 执行POW挖矿，获取满足4个0开头的哈希值的内容
    print("\n2. 开始POW挖矿，寻找以4个0开头的哈希值...")
    nickname = input("   请输入您的昵称: ")
    content, hash_result, _ = mine(nickname, 4)
    
    # 3. 使用私钥对内容进行签名
    print("\n3. 使用私钥对内容进行签名...")
    signature = sign_with_private_key(private_key, content)
    print(f"   签名完成! 签名长度: {len(signature)} 字节")
    
    # 4. 使用公钥验证签名
    print("\n4. 使用公钥验证签名...")
    is_valid = verify_with_public_key(public_key, content, signature)
    if is_valid:
        print("   签名验证成功! 内容未被篡改。")
    else:
        print("   签名验证失败! 内容可能已被篡改。")
    
    # 验证篡改内容的情况
    print("\n5. 验证篡改内容的情况...")
    tampered_content = content + "_tampered"
    is_valid = verify_with_public_key(public_key, tampered_content, signature)
    if not is_valid:
        print("   验证成功! 篡改的内容被检测到。")
    else:
        print("   验证失败! 未检测到篡改的内容。")


if __name__ == "__main__":
    main()