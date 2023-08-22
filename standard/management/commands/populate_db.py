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
                price=float(599.99),
                digital=False,
                description='Adicione estilo e funcionalidade ao seu dia com nosso elegante relógio de pulso. Com design sofisticado e precisão no movimento, este relógio combina moda e praticidade. Seja para ocasiões formais ou momentos casuais, este acessório refinado é perfeito para expressar sua personalidade única. Não deixe o tempo escapar, adquira já o seu!',
            )
            watch.image.save('watch.jpg', open("static/images/watch.jpg", "rb"))
            
            source_code = Product.objects.create(
                name='Código Fonte', 
                price=float(1200.00),
                digital=True,
                description='Explore o potencial ilimitado do nosso software inovador. Desenvolvido com tecnologias de ponta e atenção meticulosa aos detalhes, nosso código fonte é a base sólida para a criação de soluções eficazes. Combinando flexibilidade e desempenho, nosso software permite que você alcance seus objetivos com eficiência e confiança. Liberte seu potencial criativo e transforme sua visão em realidade com nosso código fonte de qualidade',
            )
            source_code.image.save('source_code.jpeg', open("static/images/source_code.jpeg", "rb"))

            books = Product.objects.create(
                name='Conjunto de Livros', 
                price=float(69.90),
                digital=False,
                description='Descubra um mundo de conhecimento e imaginação com nosso envolvente conjunto de livros. De aventuras épicas a histórias emocionantes, cada volume transporta você para universos únicos. Com escrita cativante e ilustrações fascinantes, esses livros são uma jornada que desperta a mente e alimenta a curiosidade. Uma coleção essencial para todos os amantes da leitura, abra as páginas e deixe-se mergulhar em histórias que nunca terminam.',  
            )
            books.image.save('books.png', open("static/images/books.png", "rb"))
            
            socks = Product.objects.create(
                name='Meia Estilizada', 
                price=float(45.50),
                digital=False,
                description='Complete seu visual com nossas meias estilizadas, onde conforto encontra criatividade. Com designs únicos e cores vibrantes, estas meias elevam seu estilo a um nível totalmente novo. Feitas com materiais de qualidade, proporcionam ajuste perfeito e sensação suave o dia todo. Seja uma declaração de moda ou um toque divertido, nossas meias estilizadas são a expressão perfeita da sua individualidade.',
            )
            socks.image.save('socks.jpeg', open("static/images/socks.jpeg", "rb"))

            necklace = Product.objects.create(
                name='Colar de Pedras Raras', 
                price=float(999.99),
                digital=False,
                description='Descubra a beleza singular de nosso colar de pedras raras, uma obra-prima da natureza. Cada pedra cuidadosamente selecionada é uma peça única da Terra, trazendo cores e padrões exclusivos. Este colar elegante é mais do que um acessório; é uma declaração de apreciação pela criação natural. Use-o com orgulho, sabendo que você está carregando a história da Terra ao redor do seu pescoço.',  
            )
            necklace.image.save('necklace.jpeg', open("static/images/necklace.jpeg", "rb"))
            
            katana = Product.objects.create(
                name='Katana', 
                price=float(590.00),
                digital=False,
                description='Desperte seu espírito guerreiro com nossa katana artesanal. Forjada com maestria, essa lâmina é uma combinação de tradição e excelência técnica. Sua forma elegante e afiada simboliza força e honra. Seja como uma peça de exibição ou uma ferramenta de treinamento, nossa katana personifica a arte da espada japonesa. Empunhe-a e mergulhe na história e na destreza dos samurais.',  
            )
            katana.image.save('katana.jpeg', open("static/images/katana.jpeg", "rb"))
            
            camera = Product.objects.create(
                name='Camera Semiprofissional', 
                price=float(800.90),
                digital=False,
                description='Capture momentos inesquecíveis com nossa câmera semiprofissional. Projetada para entusiastas da fotografia, essa câmera combina versatilidade e qualidade. Suas configurações avançadas oferecem controle total sobre suas imagens, enquanto sua portabilidade permite que você esteja pronto para fotografar em qualquer lugar. De retratos a paisagens, explore sua criatividade e transforme momentos em lembranças eternas com nossa câmera semiprofissional.',  
            )
            camera.image.save('camera.jpeg', open("static/images/camera.jpeg", "rb"))
            
            airplane_passage = Product.objects.create(
                name='Passagemd e Avião', 
                price=float(1399.90),
                digital=True,
                description='Abra asas para novas aventuras com nossa passagem de avião. Conecte-se a destinos emocionantes e culturas diversas enquanto você voa com conforto e conveniência. Nossa passagem oferece a liberdade de explorar, criar memórias e vivenciar o mundo de uma perspectiva única. Deixe o horizonte ser seu guia e embarque nessa jornada que ampliará seus horizontes.',  
            )
            airplane_passage.image.save('airplane_passage.jpeg', open("static/images/airplane_passage.jpeg", "rb"))
            
            bicycle = Product.objects.create(
                name='Bicicleta', 
                price=float(2000.00),
                digital=False,
                description='Explore o mundo ao seu ritmo com nossa bicicleta versátil. Projetada para aventuras urbanas e trilhas naturais, esta bicicleta oferece liberdade e saúde. Seja pedalando para o trabalho ou explorando novos caminhos, nossa bicicleta é um convite para se desconectar, se exercitar e se conectar com o ambiente ao seu redor. Uma maneira divertida e sustentável de abraçar a jornada.',  
            )
            bicycle.image.save('bicycle.jpg', open("static/images/bicycle.jpg", "rb"))
            
            self.stdout.write(
                self.style.SUCCESS('Loja carregada com sucesso :')
            )