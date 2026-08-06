
#Chat
chat = client.chats.create(model="gemini-2.0-flash", config=config_seguranca)

# Loop de Conversa
print("--- SecBot: Assistente de Segurança Iniciado (digite 'sair' para encerrar) ---")
while True:
    entrada = input("\nVocê: ").strip()
    
    if not entrada:
        continue
        
    if entrada.lower() == 'sair':
        print("SecBot encerrado.")
        break

    resposta = chat.send_message(entrada)
    print(f"\nSecBot: {resposta.text}")

