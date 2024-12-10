from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class ChatBot():
    def __init__(self, api_key, model_name):
        self.api_key = api_key
        self.model_name = model_name


    def get_response(self, history, question):
        if history:
            lst = [(x['role'], x['content']) for x in history]
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
        prompt_template += lst
        prompt_template.append(("human", "{question}"))

        prompt_template = ChatPromptTemplate.from_messages(prompt_template)

        llm = ChatOpenAI(model=self.model_name, api_key=self.api_key)
        llm_chain = prompt_template | llm

        response = llm_chain.invoke({"question": question})
        return response.content