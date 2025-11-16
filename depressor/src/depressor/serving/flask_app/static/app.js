const button = document.getElementById('predict-btn');
const input = document.getElementById('input');
const output = document.getElementById('output');

button.addEventListener('click', async () => {
  output.textContent = 'Requesting predictions...';
  const response = await fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: input.value })
  });
  const data = await response.json();
  output.textContent = JSON.stringify(data, null, 2);
});
