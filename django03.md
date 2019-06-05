django math filters

throw/ => 사용자 form

catch/ => get (인풋을 받을수 있게)


스테틱안에도 폴더를 통해 관리하는 이유는 

다른 앱의 스테틱 파일을 불러올수도있어서 

구분시켜줌


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , 'intro', 'templates')],
        
DIRS 를 바꿔준게 인트로 templates 를 가장 먼저 지나라