const tg = window.Telegram.WebApp;

document.getElementById("start-mining").addEventListener("click", () => {
    document.getElementById("status").innerText = "Майнинг запущен!";
    tg.MainButton.text = "Стоп";
    tg.MainButton.show();
});

tg.ready();
