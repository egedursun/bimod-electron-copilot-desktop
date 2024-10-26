
## BIMOD.IO - ELECTRON COPILOT - DESKTOP CLIENT
### INSTRUCTIONS AND DOCUMENTATION
#### **Author**: [Bimod.io AI as a Service](https://www.bimod.io)

---

**DJANGO ADMIN PANEL CREDENTIALS**

- **Username:** bimod

- **Password:** multimodal

---

**MIGRATING THE DATABASE:**

- Creating the Database Migrations:

```bash
python3 manage.py makemigrations
```

- Applying the Database Migrations:

```bash
python3 manage.py migrate
```

- Faking the Database Migrations:

```bash
python3 manage.py migrate --fake
```

---

**RUNNING THE APPLICATION:**

**Django Server:**

```bash
python3 manage.py runserver
```

**ElectronJS Native Application:**

```bash
sudo npx electron electron.js
```

---

### TODO LIST

- [ ] Build the dashboard (chat) page for assistants.
- [ ] Build the dashboard (chat) page for leanmods.
- [ ] Build the dashboard (chat) page for orchestrations.
- [ ] Polish the images in the UI/UX.
- [ ] Try to adjust the electron application logo.
- [ ] Try to take the first build for MacOSX (For testing)
- [ ] Create the deployment branch (along with the main).
- [ ] Build the GitHub workflow files.
- [ ] Try to deployment actions for the app on GitHub.
- [ ] Package the application for the platforms.
- [ ] Put the packages in the main (bimod.io) website.
- [ ] Implement the always on page floating copilot.
- [ ] Connect copilot functionality to chats.
- [ ] Test copilot.
- [ ] Take the second build of the application.
- [ ] Put the updated version on the website.
- [ ] Start working on features for background data retrieval.
- [ ] Start working on features for background SSH server creation.
- [ ] Try to connect to own computer with assistant connection.
- [ ] Try listening to audio recordings and speeches (for meeting integration)
- [ ] If it is working, start working on the MEETING project (KANBAN) on mainframe (bimod.io)
- [ ] Test the functionality (dashboard kanban topic creation, description creation, task assignment)
- [ ] Take the third build of the application.
- [ ] Put the updated version on the website.
- [ ] Create the automated process to take screenshots and interpret it to understand daily works (Tempo Project)
- [ ] Create the services and protocols to communicate the tempo.
- [ ] If working, start working on the TEMPO project, on mainframe (bimod.io).
- [ ] Test the functionality (tempo inspection, people task summarization, meta-reporting, performance analysis,
kanban comparison analysis, etc.)
- [ ] Take the fourth build of the application.
- [ ] Put the updated version on the website.


---
