# Alfadenta Website Restoration Guide (Technical)

This document is intended for technical personnel or automated agents to restore the Alfadenta website from a backup archive.

## Hosting Environment
- **Provider**: Interneto Vizija (IV.lt)
- **Panel**: DirectAdmin (Direct Access: `begemotas.serveriai.lt:8443`)
- **Main Domain**: alfadenta.com
- **User Root**: `/home/alfadent`

## Key Locations
- **Web Root**: `/domains/alfadenta.com/public_html`
- **Backup Storage**: `/application_backups` (Outside `public_html`)
- **Manual Backups**: `/backups`

## Restoration Process

### Using Installatron (Preferred)
1. Log in to DirectAdmin.
2. Navigate to **Advanced Features** -> **Installatron Applications Installer**.
3. Select the `alfadenta.com` application.
4. Go to the **Backups & Restore** tab.
5. Identify the backup (e.g., `2026-01-25`) and click **Restore**.
6. Follow the wizard to overwrite existing files and the database.

### Manual Restoration
If Installatron is unavailable:
1. **Archive Type**: `.tar.gz` (standard compressed archive).
2. **File Extraction**:
   - Upload the archive to `/application_backups`.
   - Use DirectAdmin File Manager to **Extract** (Išskleisti) the files.
   - Move files from the extracted directory to `/domains/alfadenta.com/public_html`.
3. **Database**:
   - If the archive contains a `.sql` file, find the database name in `wp-config.php` (if WordPress) or the relevant config file.
   - Use **phpMyAdmin** to drop existing tables and import the SQL file.

## Troubleshooting
- **Permissions**: Ensure files in `public_html` are owned by `alfadent` (UID/GID) and permissions are `644` for files and `755` for directories.
- **PHP Version**: The server is currently running **PHP 7.4**. Ensure the restored version is compatible.

---
*Created on 2026-03-06 for future reference.*
