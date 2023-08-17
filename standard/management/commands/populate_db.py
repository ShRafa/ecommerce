from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from standard.models import Product


class Command(BaseCommand):
    help = 'Carrega a loja com itens fictícios pré selecionados'
    
    def handle(self, *args, **options):
        if not User.objects.all().exists():
            User.objects.create_superuser(
                username='postgres', email='postgres@email.com', password='postgres'
            )
            self.stdout.write(
                self.style.SUCCESS(
                    'Superuser criado com sucesso login: postgres / password: postgres'
                )
            )
            
        if not Product.objects.all().exists():
            watch = Product.objects.create(
                name='Relógio', 
                price=Product.brazilianCurrency(599.99),
                digital=False,
                image='',
                description='Adicione estilo e funcionalidade ao seu dia com nosso elegante relógio de pulso. Com design sofisticado e precisão no movimento, este relógio combina moda e praticidade. Seja para ocasiões formais ou momentos casuais, este acessório refinado é perfeito para expressar sua personalidade única. Não deixe o tempo escapar, adquira já o seu!',
            )
            source_code = Product.objects.create(
                name='Código Fonte', 
                price= Product.brazilianCurrency(1200.00),
                digital=True,
                image='',
                description='Explore o potencial ilimitado do nosso software inovador. Desenvolvido com tecnologias de ponta e atenção meticulosa aos detalhes, nosso código fonte é a base sólida para a criação de soluções eficazes. Combinando flexibilidade e desempenho, nosso software permite que você alcance seus objetivos com eficiência e confiança. Liberte seu potencial criativo e transforme sua visão em realidade com nosso código fonte de qualidade',
            )
            books = Product.objects.create(
                name='Conjunto de Livros', 
                price=Product.brazilianCurrency(69.90),
                digital=False,
                image='',
                description='Descubra um mundo de conhecimento e imaginação com nosso envolvente conjunto de livros. De aventuras épicas a histórias emocionantes, cada volume transporta você para universos únicos. Com escrita cativante e ilustrações fascinantes, esses livros são uma jornada que desperta a mente e alimenta a curiosidade. Uma coleção essencial para todos os amantes da leitura, abra as páginas e deixe-se mergulhar em histórias que nunca terminam.',  
            )
            socks = Product.objects.create(
                name='Meia Estilizada', 
                price=Product.brazilianCurrency(45.50),
                digital=False,
                image='',
                description='Complete seu visual com nossas meias estilizadas, onde conforto encontra criatividade. Com designs únicos e cores vibrantes, estas meias elevam seu estilo a um nível totalmente novo. Feitas com materiais de qualidade, proporcionam ajuste perfeito e sensação suave o dia todo. Seja uma declaração de moda ou um toque divertido, nossas meias estilizadas são a expressão perfeita da sua individualidade.',
            )
            necklace = Product.objects.create(
                name='Colar de Pedras Raras', 
                price=Product.brazilianCurrency(999.99),
                digital=False,
                image='',
                description='Descubra a beleza singular de nosso colar de pedras raras, uma obra-prima da natureza. Cada pedra cuidadosamente selecionada é uma peça única da Terra, trazendo cores e padrões exclusivos. Este colar elegante é mais do que um acessório; é uma declaração de apreciação pela criação natural. Use-o com orgulho, sabendo que você está carregando a história da Terra ao redor do seu pescoço.',  
            )
            katana = Product.objects.create(
                name='Katana', 
                price=Product.brazilianCurrency(590.00),
                digital=False,
                image='',
                description='Desperte seu espírito guerreiro com nossa katana artesanal. Forjada com maestria, essa lâmina é uma combinação de tradição e excelência técnica. Sua forma elegante e afiada simboliza força e honra. Seja como uma peça de exibição ou uma ferramenta de treinamento, nossa katana personifica a arte da espada japonesa. Empunhe-a e mergulhe na história e na destreza dos samurais.',  
            )
            camera = Product.objects.create(
                name='Camera Semiprofissional', 
                price=Product.brazilianCurrency(800.90),
                digital=False,
                image='',
                description='Capture momentos inesquecíveis com nossa câmera semiprofissional. Projetada para entusiastas da fotografia, essa câmera combina versatilidade e qualidade. Suas configurações avançadas oferecem controle total sobre suas imagens, enquanto sua portabilidade permite que você esteja pronto para fotografar em qualquer lugar. De retratos a paisagens, explore sua criatividade e transforme momentos em lembranças eternas com nossa câmera semiprofissional.',  
            )
            airplane_passage = Product.objects.create(
                name='Passagemd e Avião', 
                price=Product.brazilianCurrency(1399.90),
                digital=True,
                image='',
                description='Abra asas para novas aventuras com nossa passagem de avião. Conecte-se a destinos emocionantes e culturas diversas enquanto você voa com conforto e conveniência. Nossa passagem oferece a liberdade de explorar, criar memórias e vivenciar o mundo de uma perspectiva única. Deixe o horizonte ser seu guia e embarque nessa jornada que ampliará seus horizontes.',  
            )
            bicycle = Product.objects.create(
                name='Bicicleta', 
                price=Product.brazilianCurrency(2000.00),
                digital=False,
                image='',
                description='Explore o mundo ao seu ritmo com nossa bicicleta versátil. Projetada para aventuras urbanas e trilhas naturais, esta bicicleta oferece liberdade e saúde. Seja pedalando para o trabalho ou explorando novos caminhos, nossa bicicleta é um convite para se desconectar, se exercitar e se conectar com o ambiente ao seu redor. Uma maneira divertida e sustentável de abraçar a jornada.',  
            )
            self.stdout.write(
                self.style.SUCCESS('Loja carregada com sucesso :)')
            )