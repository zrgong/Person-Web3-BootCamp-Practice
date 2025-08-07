simulated_blockchain.py的运行说明：
1、安装依赖：
pip install flask

2、运行服务器：
python simulated_blockchain.py
运行日志：
PS D:\code\blockchain\Person-Web3-BootCamp-Practice\Model_1_Blockchain_fundamentals> python simulated_blockchain.py
 * Serving Flask app 'simulated_blockchain'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.26.2.29:5000
Press CTRL+C to quit
127.0.0.1 - - [07/Aug/2025 15:46:59] "GET /mine HTTP/1.1" 200 -
127.0.0.1 - - [07/Aug/2025 15:47:18] "GET /mine HTTP/1.1" 200 -


3、使用 curl 测试 /mine 路由：
curl http://127.0.0.1:5000/mine
运行日志：
PS D:\code\blockchain\Person-Web3-BootCamp-Practice> curl http://127.0.0.1:5000/mine
                                                                                                  
                                                                                                  
StatusCode        : 200                                                                           
StatusDescription : OK                                                                            
Content           : {"index":2,"message":"New Block Forged","previous_hash":"4e6e36016fc365eee054
                    a8c751f092a1a6f6cbd836327639398dbe003db013ec","proof":35293,"transactions":[{
                    "amount":1,"recipient":"078a4df03fe242b2a83a02...
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 228
                    Content-Type: application/json
                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {"index":2,"message":"New Block Fo...
                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1
                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1
                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {"index":2,"message":"New Block Fo...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 228], [Content-Type, application/json]    
                    , [Date, Thu, 07 Aug 2025 07:46:59 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 228


                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {"index":2,"message":"New Block Fo...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 228], [Content-Type, application/json]    
                    , [Date, Thu, 07 Aug 2025 07:46:59 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 228

                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {"index":2,"message":"New Block Fo...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 228], [Content-Type, application/json]    
                    , [Date, Thu, 07 Aug 2025 07:46:59 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {"index":2,"message":"New Block Fo...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 228], [Content-Type, application/json]    
                    , [Date, Thu, 07 Aug 2025 07:46:59 GMT]...}
Images            : {}
InputFields       : {}
                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {"index":2,"message":"New Block Fo...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 228], [Content-Type, application/json]    
                    , [Date, Thu, 07 Aug 2025 07:46:59 GMT]...}
                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {"index":2,"message":"New Block Fo...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 228], [Content-Type, application/json]    
                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    {"index":2,"message":"New Block Fo...
                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1

                    Date: Thu, 07 Aug 2025 07:46:59 GMT
                    Server: Werkzeug/3.1.3 Python/3.13.1


                    {"index":2,"message":"New Block Fo...
                    {"index":2,"message":"New Block Fo...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 228], [Content-Type, application/json]
                    , [Date, Thu, 07 Aug 2025 07:46:59 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 228



PS D:\code\blockchain\Person-Web3-BootCamp-Practice>