# 入口文件
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # 设置IP
        port=5000,  # 设置端口号
        debug=app.config['DEBUG'],  # 开启Debug模式，保存后服务器自动重启
        threaded=True  # 开启多线程
    )
