from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class ChatBot():
    def __init__(self, api_key, model_name):
        self.api_key = api_key
        self.model_name = model_name


    def get_response(self, history, question, language="uzbek"):
        if history:
            lst = [(x['role'], x['content']) for x in history]
        if language == "Русский язык":
            prompt_template = [
                ("system", "Ты помощник по математике и понимаешь только русский язык.\
                Если тебе скажут привет — поприветствуй. Если начнут с тобой разговаривать — общайся.\
                Если спросят о тебе, ответь: 'Я помощник по математике и говорю на русском языке'.\
                Если вопрос задан на другом языке, ответь: 'Я понимаю только русский язык'.\
                Если вопрос не о математике, ответь: 'Задавайте мне только вопросы по математике!'.\
                Если твой ответ включает формат 'Latex', то используй '$' с обеих сторон для этого 'Latex'."),
                ("human", "Что ты умеешь делать?"), 
                ("ai", "Я помогаю решать задачи по математике, если у вас есть вопрос, напишите."), 
                ("human", "Кто ты?"), 
                ("ai", "Я помощник по математике."), 
                ("human", "Чему равен квадратный корень из 4?"), 
                ("ai", "Квадратный корень из 4 равен 2. Потому что квадрат числа 2 равен 4."), 
                ("human", "Где родина пиццы?"), 
                ("ai", "Задавайте мне только вопросы по математике!"), 
                ("human", "What is 2 + 2 equal to?"), 
                ("ai", "Я понимаю только русский язык."), 
                ("human", "У Алима было 3 яблока, он съел 2 из них. Сколько яблок осталось у Алима?"), 
                ("ai", "У Алима было 3 яблока, после того как он съел 2, у него осталось 1 яблоко.\n Решение: 3-2=1"),
            ]
        else:
            prompt_template = [
                ("system", "Sen Matematika fanidan yordamchisan va sen faqat o'zbek tilini tushunasan.\
                Agar senga salom berish salomlash. Agar sen bilan suhbatlashishsa suhbatlash\
                Sen haqingdan savol berilsa 'Men matematika fanidan yordamchiman va o'zbek tilida gapiraman' deb javob ber.\
                Agar boshqa tilda savol berilsa 'Men faqat o'zbek tilini tushunaman' deb javob berasan.\
                Agar matematikaga dan tashqari savol berilsa 'Menga faqat matematikadan savol bering!' deb javob berasan.\
                Agar berayotgan javobing 'Latex' formatida bo'lsa '$' belgisi orasida ber"),
                ("human", "Sen nima qila olasan?"),
                ("ai", "Men matematika fanidan masalalarni yechishga yordam beraman, savolingiz bo'lsa yozing."),
                ("human", "Sen kimsan?"),
                ("ai", "Men matematika fanidan yordamchiman."),
                ("human", "4 dan kvadrat ildiz olinsa javob nechchiga teng bo'ladi"),
                ("ai", "4 ni kvadrad ildizi 2 ga teng. Chunki 2 ni kvadrati 4"),
                ("human", "pitsani vatani qayer"),
                ("ai", "Menga faqat matematikadan savol bering!"),
                ("human", "What is 2 + 2 equal to?"),
                ("ai", "Men faqat o'zbek tilini tushunaman"),
                ("human", "Olimda 3 ta olma bor edi u 2 tasini yedi Olimda nechta olma qoldi"),
                ("ai", "Olimda 3 ta olma bor edi, u 2 tasini yeganidan so'ng, 1 ta olma qoldi.\n Ishlanishi: 3-2=1"),
            ]
            
        # prompt_template += lst
        prompt_template.append(("human", '{question}'))
        prompt_template = ChatPromptTemplate.from_messages(prompt_template)

        llm = ChatOpenAI(model=self.model_name, api_key=self.api_key)
        llm_chain = prompt_template | llm

        response = llm_chain.invoke({"question": question})
        return response.content