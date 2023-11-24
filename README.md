# Illtracker device
![Logoilltracker](/illtrackerlogo.png)

## Sumário
- [Problemas na hora do checkup](#problemas-na-hora-do-checkup)
- [A nossa proposta](#a-nossa-proposta)
- [Exemplos do projeto](#imagem-exemplificando-o-projeto-montado)
- [Planos Para o futuro](#instalação)
- [Configurações](#configurações)
- [Como executar](#como-executar)
## Problemas na hora do checkup
Quando vamos a um hospital quando nos sentimos mal, explicamos o que estamos sentindo no momento, mas quando o médico pergunta sobre mais detalhes ou também se sentimos alguns outros sintomas em outras datas, a nossa memória falhar.

## A nossa proposta
Em meio ao dinâmico universo dos serviços de saúde, surge uma necessidade crucial: o eficiente gerenciamento das informações dos pacientes. Apresentamos o "illTracker", um aplicativo inovador que simplifica o registro diário de sintomas e medicamentos. Os pacientes registram sua jornada de saúde, eliminando redundâncias. Ao chegar ao hospital, basta fornecer o código, permitindo a recuperação instantânea de informações relevantes. Isso não apenas reduz questionamentos extensos durante as consultas, mas também promove eficiência e uma abordagem personalizada no tratamento. O "illTracker" está aqui para aprimorar a eficácia do atendimento médico e elevar a experiência do paciente a novos patamares.

### Imagem exemplificando o projeto montado
![Imagem Arduino Montado](/hardware.png)

### Código do arduino comentado
Deve-se alterar o SSID e a senha da rede como o projeto está no seu começo de desenvolvimento [Link para Código ESP32](/illtracker.ino)

## Instalação
1. Clone este repositório.
2. Abra o arquivo [illtracker.ino](/illtracker.ino) na Arduino IDE.
3. Instale as bibliotecas necessárias usando o Gerenciador de Bibliotecas da Arduino IDE.
4. Configure o SSID e senha da rede, e o ID do seu dispositivo
5. Carregue o código para o Esp32.

## Configurações
No arquivo [illtracker.ino](/illtracker.ino), você pode configurar o seguinte:
- SSID e senha da rede WiFi.
- ID do dispositivo

## Como executar
1. Caso faça pelo Wokwi, apenas mantenha o SSID e a senha como estão. Caso esteja montando uma versão física, configure para o Wi-Fi de sua preferência.
2. Basta apertar o botão para registrar as medidas em nosso sistema.
3. Ao usar o aplicativo, será usado a medida mais recente e ficará salvo em um banco de dados.
