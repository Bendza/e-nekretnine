const { app, BrowserWindow, ipcMain } = require('electron');
const { fetchData } = require('./mongo');

let mainWindow = null;

app.on('ready', createWindow);

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1300,
        height: 900,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            enableRemoteModule: true
        }
    });

    mainWindow.loadFile('../index.html');

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

ipcMain.on('request-data', async (event) => {
    try {
        const data = await fetchData();
        event.sender.send('data-response', data);
    } catch (err) {
        event.sender.send('data-response', { error: err.message });
    }
});

ipcMain.on('apply-filters', async (event, filters) => {
    console.log("Received filters:", filters);  // New line
    try {
        const data = await fetchData(filters);
        event.sender.send('data-response', data);
    } catch (err) {
        event.sender.send('data-response', { error: err.message });
    }
});
