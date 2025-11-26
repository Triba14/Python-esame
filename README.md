# Blog Django

Blog fatto con Django. Si possono creare, vedere, modificare e cancellare i post.

## Funzionalità

- Creare nuovi post dall'admin
- Vedere tutti i post pubblicati nella homepage
- Leggere i dettagli di ogni post
- Modificare i post dall'admin
- Cancellare i post dall'admin
- Aggiungere immagini ai post

## Come farlo partire

Installa le librerie:
```
pip install -r requirements.txt
```

Vai nella cartella mysite:
```
cd mysite
```

Fai le migrazioni:
```
python manage.py migrate
```

Crea un utente admin:
```
python manage.py createsuperuser
```

Avvia il server:
```
python manage.py runserver
```

Poi apri http://127.0.0.1:8000/ nel browser

## Screenshot

![Screenshot 1](screenshots/screenshot-2025-11-21_16-41-40.png)

![Screenshot 2](screenshots/screenshot-2025-11-21_16-42-12.png)

![Screenshot 3](screenshots/screenshot-2025-11-21_16-42-42.png)

![Screenshot 4](screenshots/screenshot-2025-11-21_16-43-37.png)

![Screenshot 5](screenshots/screenshot-2025-11-21_16-44-58.png)

![Screenshot 6](screenshots/screenshot-2025-11-21_16-45-44.png)
