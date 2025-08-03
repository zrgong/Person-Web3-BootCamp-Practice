import hashlib
import time

#模块一： 区块链基础
#实战 1：编码模拟工作量证明（ POW ）过程 与非对称加密应用

def mine(nickname, difficulty):
    """执行POW挖矿，直到找到满足难度要求的哈希值"""
    target = '0' * difficulty
    nonce = 0
    start_time = time.time()
    
    while True:
        # 构建要哈希的内容
        content = f"{nickname}{nonce}"
                # 将 content 字符串编码为字节类型，因为 hashlib.sha256() 方法需要字节对象作为输入
        # encode() 方法默认使用 utf-8 编码将字符串转换为字节
        encoded_content = content.encode()
        # 使用 hashlib.sha256() 函数创建一个 SHA-256 哈希对象，传入编码后的内容进行哈希计算
        sha256_hash = hashlib.sha256(encoded_content)
        # 使用 hexdigest() 方法将哈希对象转换为十六进制字符串，方便查看和比较
        hash_result = sha256_hash.hexdigest()

        # 也可以用以下一行计算SHA256哈希
        # hash_result = hashlib.sha256(content.encode()).hexdigest()

        # 检查是否满足难度要求
        if hash_result.startswith(target):
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("nonce的内容是:", nonce)
            return content, hash_result, elapsed_time
        
        nonce += 1

def main():
    nickname = input("请输入您的昵称: ")
    
    #  mining for 4 zeros
    print(f"开始挖矿，寻找以4个0开头的哈希值...")
    content4, hash4, time4 = mine(nickname, 4)
    print(f"找到4个0开头的哈希值! 耗时: {time4:.4f}秒")
    print(f"内容: {content4}")
    print(f"哈希值: {hash4}")
    print()
    
    #  mining for 5 zeros
    print(f"开始挖矿，寻找以5个0开头的哈希值...")
    content5, hash5, time5 = mine(nickname, 5)
    print(f"找到5个0开头的哈希值! 耗时: {time5:.4f}秒")
    print(f"内容: {content5}")
    print(f"哈希值: {hash5}")


if __name__ == "__main__":
    main()