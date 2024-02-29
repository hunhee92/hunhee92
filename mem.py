import hashlib

class Member:
    def __init__(self, name, username, password):
        hashpass=hashlib.sha256(password.encode())
        h_pass = hashpass.hexdigest()
        self.name = name
        self.username = username
        self.password = h_pass

        

    def display(self):
        print(f"{self.name}{self.username}")
        

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


members = []

members.append(Member("쌍봉", "낙타", "asdf"))
members.append(Member("나무", "늘보", "1234"))
members.append(Member("하이", "에나", "qwe123"))


for member in members:
    print(member.name )
    #member.display()
    
# 6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
#     1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
#     2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
posts = []
for member in members :
    
    for i in range(1,4) : 
        post =Post(f"제목 : {member.name}{i}" ,f"내용 : {member.username}" , member.username)
        posts.append(post)
        
fname = "낙타"
for post in posts :

    if post.author ==  fname :
        print(post.title)   
        

fcontent = "늘보"
for post in posts :
    
    if fcontent in post.content : 
        print(post.title)          

# **추가 도전 과제:**

# 1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
# 2. post도 터미널에서 생성할 수 있게 해주세요.
# 3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.


n_name =input("이름 :")
n_username =input("아이디 :")
n_password = input("비밀번호 :")

n_member = Member(n_name, n_username, n_password)
members.append(n_member)

for member in members:
    print(member.name)
    
n_title = input("제목 :")
n_content = input("내용 :")
n_author = input("글쓴이:")
n_con = Post(n_title,n_content,n_author)
posts.append(n_con)

for post in posts :

        print(post.title)   
        