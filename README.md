<div align='center'>
  
  <img width="280" src="https://user-images.githubusercontent.com/60857927/140621052-7c7ade3f-71b9-405a-a8b5-f33e3e2cc19b.png" />
  
</div>

<div align = "center">

<p>

  <a href="#descricao">Descrição</a> &#xa0; | &#xa0;
  <a href="#tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#requisitos">Requisitos</a> &#xa0; | &#xa0;
  <a href="#executando">Executando</a> &#xa0; | &#xa0;
  <a href="#referencias">Referências</a>

</p>

</div>

<div id = "descricao">

## :pushpin: Descrição ##

<p>

  Esse é o repositório do Small Web App, uma pequena aplicação web que tem como finalidade 
  estudar mais sobre como funciona os requests e responses feitos pelos servidores. A ideia
  inicial é ter uma aplicação **rápida** e **fácil** sem a utilização de frameworks.

</p>

</div>

<div id = "tecnologias">

## :rocket: Tecnologias ##

Todas as tecnologias usadas na realização do projeto:

* [Python][python] [Versão 3.8]
* [PyCharm][pycharm]

</div>

<div id = "requisitos">

## :warning: Requisitos ##

<p>

  Antes de executar, você precisar ter o [Git][git] e o [Python][python] (Versão 3.8) 
  instalados na sua máquina.

</p>

</div>

<div id = "executando">

## :computer: Executando ##

<p>

  Depois de correr tudo certo na instalação, está na hora de clonar o repositório.

</p>

```bash
# Clone este projeto
$ git clone https://github.com/Iuri-Almeida/small-web-app.git
# Acesse a pasta do projeto
$ cd small-web-app
```

<p>

  Além disso, depois de instalado o Python e clonado o repositório, é preciso instalar a
  única depenência do projeto, o [Gunicorn][gunicorn].

</p>

```bash
# Certifique-se que o 'pip' está instalado
$ pip -V
# Instale a dependência
$ pip install -r requirements.txt
# Inicie o servidor
$ gunicorn server:app --reload
# Por padrão, será aberto em http://127.0.0.1:8000
  ```

</div>

<div id = "referencias">

## :key: Referências ##

Alguns locais de onde me baseei para realizar o projeto:

* [A Python Web App without a Framework - CodingEntrepreneurs][video]

:mag: &#xa0; Os ícones usados nesse README foram tirados desse [repositório][icones].

</div>

<!-- Links -->
[video]: https://www.youtube.com/watch?v=fe9t9DGPBuE
[vertigo]: https://vertigo.com.br/
[perfil]: https://github.com/Iuri-Almeida
[python]: https://www.python.org/
[pycharm]: https://www.jetbrains.com/pycharm/
[gunicorn]: https://gunicorn.org/
[git]: https://git-scm.com
[icones]: https://gist.github.com/rxaviers/7360908