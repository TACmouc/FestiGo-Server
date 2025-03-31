# Commandes Utiles pour FestiGo-Server

### Bien installer pip3
```bash
sudo apt install python3-pip
```

## Gestion du Service Systemd

### Activer le service au démarrage
```bash
sudo systemctl enable festigo-server.service
```

### Démarrer le service
```bash
sudo systemctl start festigo-server.service
```

### Redémarrer le service
```bash
sudo systemctl restart festigo-server.service
```

### Arrêter le service
```bash
sudo systemctl stop festigo-server.service
```

### Vérifier l'état du service
```bash
sudo systemctl status festigo-server.service
```

### Voir les journaux du service
```bash
journalctl -u festigo-server.service
```

---

## Tester l'envoi d'un email

### Envoyer un email de test avec `msmtp`
```bash
echo -e "Subject: Test Email\n\nThis is a test email." | msmtp le.bosgiraud@gmail.com
```

### Vérifier les journaux de `msmtp`
```bash
cat ~/.msmtp.log
```

---

## Tester le script `crash-alert.sh`

### Exécuter le script manuellement
```bash
bash /home/ubuntu/FestiGo-Server/crash-alert.sh
```

### Vérifier les journaux du script
```bash
cat /tmp/crash-alert.log
```

---

## Déboguer les Permissions

### Vérifier les permissions du script
```bash
ls -l /home/ubuntu/FestiGo-Server/crash-alert.sh
```

### Rendre le script exécutable
```bash
sudo chmod +x /home/ubuntu/FestiGo-Server/crash-alert.sh
```

### Vérifier les permissions du répertoire
```bash
ls -ld /home/ubuntu/FestiGo-Server
```

### Changer le propriétaire du répertoire
```bash
sudo chown -R ubuntu:ubuntu /home/ubuntu/FestiGo-Server
```

---

## Déploiement avec GitHub Actions

### Relancer le workflow GitHub Actions
1. Accédez à l'onglet **Actions** dans votre dépôt GitHub.
2. Sélectionnez le workflow **Deploy to VPS**.
3. Cliquez sur **Run workflow** pour relancer le déploiement.

---

## Redémarrer le VPS

### Redémarrer le serveur
```bash
sudo reboot
```

### Vérifier que le service redémarre automatiquement
```bash
sudo systemctl status festigo-server.service
```
