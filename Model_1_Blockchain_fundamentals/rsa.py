import hashlib
import time
# 导入加密相关的库
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

# 模块一：区块链基础
# 实战 1：编码模拟工作量证明（POW）过程与非对称加密应用


# ---------------------------- RSA 密钥生成函数 ----------------------------

def generate_rsa_keys():
    """
    生成RSA公私钥对
    
    返回:
        private_key (rsa.RSAPrivateKey): 生成的私钥对象
        public_key (rsa.RSAPublicKey): 生成的公钥对象
    """
    # 生成私钥
    # public_exponent=65537 是常用的公共指数，提供了安全性和性能的平衡
    # key_size=2048 表示密钥长度为2048位，是目前广泛使用的安全长度
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    # 从私钥中提取公钥
    public_key = private_key.public_key()
    return private_key, public_key


# ---------------------------- POW 挖矿函数 ----------------------------

def mine(nickname, difficulty):
    """
    执行工作量证明(POW)挖矿，直到找到满足难度要求的哈希值
    
    参数:
        nickname (str): 用户昵称
        difficulty (int): 难度系数，表示需要找到以多少个0开头的哈希值
    
    返回:
        content (str): 满足条件的内容 (昵称+nonce)
        hash_result (str): 计算得到的哈希值
        elapsed_time (float): 挖矿所花费的时间(秒)
    """
    # 设置目标前缀，难度系数为n则需要n个0开头
    target = '0' * difficulty
    # 初始化随机数nonce
    nonce = 0
    # 记录开始时间
    start_time = time.time()
    
    # 循环计算哈希值，直到找到满足条件的结果
    while True:
        # 构建要哈希的内容: 昵称 + nonce
        content = f"{nickname}{nonce}"
        # 将内容编码为字节，并计算SHA256哈希值
        hash_result = hashlib.sha256(content.encode()).hexdigest()
        
        # 检查哈希值是否满足难度要求（以指定数量的0开头）
        if hash_result.startswith(target):
            # 找到满足条件的哈希值，记录结束时间
            end_time = time.time()
            elapsed_time = end_time - start_time
            # 打印结果信息
            print(f"找到满足难度要求的哈希值! 耗时: {elapsed_time:.4f}秒")
            print(f"内容: {content}")
            print(f"哈希值: {hash_result}")
            print(f"nonce: {nonce}")
            return content, hash_result, elapsed_time
        
        # 增加nonce，继续尝试
        nonce += 1


# ---------------------------- 私钥签名函数 ----------------------------

def sign_with_private_key(private_key, data):
    """
    使用私钥对数据进行签名
    
    参数:
        private_key (rsa.RSAPrivateKey): 私钥对象
        data (str): 需要签名的数据
    
    返回:
        signature (bytes): 生成的签名
    """
    # 使用私钥对数据进行签名
    # padding.PSS 是一种安全的填充方案
    # mgf=padding.MGF1(hashes.SHA256()) 指定了掩码生成函数
    # salt_length=padding.PSS.MAX_LENGTH 使用最大长度的盐
    signature = private_key.sign(
        data.encode(),  # 将字符串数据编码为字节
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()  # 指定哈希算法
    )
    return signature


# ---------------------------- 公钥验证函数 ----------------------------

def verify_with_public_key(public_key, data, signature):
    """
    使用公钥验证签名
    
    参数:
        public_key (rsa.RSAPublicKey): 公钥对象
        data (str): 原始数据
        signature (bytes): 要验证的签名
    
    返回:
        bool: 验证是否成功
    """
    try:
        # 使用公钥验证签名
        # 注意这里的参数要与签名时使用的参数一致
        public_key.verify(
            signature,
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True  # 验证成功
    except:
        return False  # 验证失败


# ---------------------------- 主函数 ----------------------------

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
    
    # 5. 验证篡改内容的情况
    print("\n5. 验证篡改内容的情况...")
    tampered_content = content + "_tampered"
    is_valid = verify_with_public_key(public_key, tampered_content, signature)
    if not is_valid:
        print("   验证成功! 篡改的内容被检测到。")
    else:
        print("   验证失败! 未检测到篡改的内容。")


# 如果直接运行此脚本，则执行main函数
if __name__ == "__main__":
    main()