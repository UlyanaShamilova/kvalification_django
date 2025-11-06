async function sendMessage(message) {
  const response = await fetch('/chat/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message: message })
  });
  const data = await response.json();
  console.log('Ответ ИИ:', data.reply);
  // Выведите `data.reply` в чат на страницу
}
