## BIMOD.IO - ELECTRON COPILOT - DESKTOP CLIENT

### INSTRUCTIONS AND DOCUMENTATION

#### **Author**: [Bimod.io AI as a Service](https://www.bimod.io)

---

**DEPENDENCIES:**

- These will be needed to installed by an Bash script for the functions to work properly.

```bash
brew install sox
```

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

- [ ] Commit and push the dev branch.
- [ ] Switch to main, merge dev into main, commit and push main.
- [ ] Switch to v1_0_0, merge main into v1_0_0, commit and push v1_0_0.
- [ ] Update the env files in the v_1_0_0 branch.
- [ ] Update the README.md file.
- [ ] Commit and push the v1_0_0 branch.
- [ ] Get builds for the v1_0_0 release.
- [ ] Put the builds on AWS buckets (a new bucket for releases)
- [ ] Make sure the bucket has open access permissions.
- [ ] Test downloading process to see if it works.
- [ ] Design the web page to download the Electron Copilot (and marketing content)
- [ ] Develop Content on Main Landing Page + Connect the page with the main page. (MetaKanban, Project/Teams, MetaTempo)
- [ ] Push the changes in the main server.
- [ ] Create a label for version on GitHub
- [ ] Update the GitHub board.

---

**RELEASE 5**

---
