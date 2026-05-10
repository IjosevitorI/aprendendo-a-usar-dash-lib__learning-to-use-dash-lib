# aprendendo-a-usar-dash-lib__learning-to-use-dash-lib
código feito com o intuito de aprender a usar a biblioteca dash de visualização\\Code written with the intention of learning how to use the Dash library.

Este projeto é uma aplicação web interativa desenvolvida em Python para visualizar e exportar dados de séries temporais (como temperatura, nível do rio e índice NDVI).
O código foi construído em formato modular para facilitar a leitura e a manutenção, separando a lógica de tratamento de dados, a interface visual e os controles de ação.
As ferramentas escolhidas para este projeto priorizam a facilidade de criar uma interface funcional usando apenas Python:

## Tecnologias Adotadas e Por Quê

-Pandas: É a ferramenta que ja eu ja havia utilizado antes, e novamente utilizei para leitura, manipulação e tratamento de dados em formato de tabela. o Pandas aqui tambem foi usado para carregar os dados de texto e realizar a interpolação linear de forma automática, preenchendo as lacunas de dados vazios.
-Plotly Express: Biblioteca focada em visualização de dados. Foi escolhida porque gera gráficos interativos por padrão (permite dar zoom e passar o mouse para ler os valores exatos) escrevendo muito poucas linhas de código.
-Dash: Um framework que transforma scripts de análise de dados em aplicações web. Ele foi utilizado porque permite criar a interface visual (menus suspensos, botões e layout) diretamente em Python, sem a necessidade de construir um sistema separado em HTML, CSS ou JavaScript.


# learning-to-use-dash-lib
Code written with the intention of learning how to use the Dash library.

This project is an interactive web application developed in Python to visualize and export time series data (such as temperature, river level, and NDVI index).

The code was built in a modular format to facilitate reading and maintenance, separating the data processing logic, the visual interface, and the action controls.

The tools chosen for this project prioritize the ease of creating a functional interface using only Python:

## Technologies Adopted and Why

-Pandas: This is a tool I had used before, and I used it again for reading, manipulating, and processing data in table format. Pandas was also used here to load text data and perform linear interpolation automatically, filling in empty data gaps.
-Plotly Express: A library focused on data visualization. It was chosen because it generates interactive graphs by default (allowing zooming and hovering to read exact values) while requiring very few lines of code.
-Dash: A framework that transforms data analysis scripts into web applications. It was used because it allows creating the visual interface (dropdown menus, buttons, and layout) directly in Python, without the need to build a separate system in HTML, CSS, or JavaScript.


## Instruções de execução

a linguagem de programação utilizada para a escrita do codigo fonte foi o Python (especificamente a versão 3.14.4)
a versão mais recente pode ser encontrada no site oficial do Python. https://www.python.org/

as bibliotecas usadas e necessarias para a execução do codigo são as seguintes: dash, pandas e plotly.
No terminal (no Linux/Mac) ou Prompt de Comando / PowerShell (no Windows) digite o seguinte comando para instalar as bibliotecas utilizando o pip:
`pip install dash pandas`
ao fazer a instalação da biblioteca dash a biblioteca plotly e instalada em conjunto.

No terminal, navegue até a pasta onde você salvou o arquivo dashing.py e execute o script com o comando:
`python dashing.py`
Se tudo der certo, o terminal vai exibir uma mensagem indicando que o servidor está rodando (algo como "Dash is running on http://127.0.0.1:8050/").
Abra o seu navegador de internet de preferência e acesse o endereço


## Execution Instructions

The programming language used to write the source code was Python (specifically version 3.14.4).
The latest version can be found on the official Python website: https://www.python.org/

The libraries used and necessary for running the code are: dash, pandas, and plotly.

In the terminal (on Linux/Mac) or Command Prompt / PowerShell (on Windows), type the following command to install the libraries using pip:
`pip install dash pandas`
When installing the dash library, the plotly library is installed along with it.

In the terminal, navigate to the folder where you saved the dashing.py file and run the script with the command:
`python dashing.py`
If everything goes well, the terminal will display a message indicating that the server is running (something like "Dash is running on http://127.0.0.1:8050/").
Open your preferred internet browser and go to the address.


## Usando a Interface

O dashboard possui duas funções principais:
-Visualização Dinâmica: No menu superior, escolha entre Temperatura, Nível do Rio ou NDVI. O gráfico será atualizado automaticamente, mostrando a evolução da métrica no tempo junto com uma linha tracejada indicando o valor médio.
-Exportação de Dados: Na parte inferior, você pode escolher um critério de ordenação (por exemplo, "Temperatura Crescente") e clicar no botão "Gerar CSV". Isso fará com que os dados organizados sejam impressos no seu terminal e um novo arquivo .csv seja salvo automaticamente na mesma pasta do projeto.


## Using the Interface

The dashboard has two main functions:
- Dynamic Visualization: In the top menu, choose between Temperature, River Level, or NDVI. The graph will update automatically, showing the evolution of the metric over time along with a dashed line indicating the average value.
- Data Export: At the bottom, you can choose a sorting criterion (for example, "Increasing Temperature") and click the "Generate CSV" button. This will cause the organized data to be printed to your terminal and a new .csv file to be automatically saved in the same project folder.
