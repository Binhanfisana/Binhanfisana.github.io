from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    context = {
        'page_title': 'Binhan | Redes, OpenRAN e 5G',
        'hero_text': 'Mestrando em Ciência da Computação na UFSCar. Pesquiso OpenRAN e 5G, com a experiência de quem já mediu fibra em campo.',
        'sections': [
            {
                'title': 'Redes móveis',
                'description': 'OpenRAN, 5G, arquiteturas abertas de acesso por rádio.'
            },
            {
                'title': 'Redes ópticas',
                'description': 'FTTH/GPON, fusão óptica, medições com OTDR, trabalho de campo.'
            },
            {
                'title': 'Software e infraestrutura',
                'description': 'Linux, Python, Git, Terraform e AWS. Ajuste esta lista com o que você realmente usa.'
            },
        ],
        'projects': [
            {
                'title': 'tfgoat-aws',
                'url': 'https://github.com/Binhanfisana/tfgoat-aws',
                'description': 'Fork de estudo: infraestrutura AWS vulnerável em Terraform, para praticar segurança em cloud.',
            },
            {
                'title': 'Seu próximo projeto',
                'url': '#',
                'description': 'Troque por um projeto seu, com link para o repositório e uma frase sobre o que ele faz.',
            },
            {
                'title': 'Pesquisa de mestrado',
                'url': '#',
                'description': 'Parte do trabalho é feita com parceiros e não pode ser publicada. Links para artigos entram aqui quando houver.',
            },
        ],
        'contact_links': [
            {'label': 'GitHub', 'url': 'https://github.com/Binhanfisana'},
            {'label': 'LinkedIn', 'url': 'https://www.linkedin.com/in/SEU-USUARIO'},
            {'label': 'Lattes', 'url': 'http://lattes.cnpq.br/SEU-ID'},
            {'label': 'seu.email@exemplo.com', 'url': 'mailto:seu.email@exemplo.com'},
        ],
    }
    return render(request, 'home.html', context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def projects(request: HttpRequest) -> HttpResponse:
    return render(request, 'projects.html', {'projects': [
        {'title': 'tfgoat-aws', 'description': 'Infraestrutura AWS vulnerável em Terraform para aprendizado de segurança em cloud.', 'url': 'https://github.com/Binhanfisana/tfgoat-aws'},
        {'title': 'Pesquisa de mestrado', 'description': 'Trabalho acadêmico em redes móveis e OpenRAN com foco em arquitetura 5G.', 'url': '#'},
    ]})


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')
