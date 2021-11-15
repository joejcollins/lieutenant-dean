/**
 * Run up the Unleash Proxy with the configuration from the parent directory.
 */
require('dotenv').config({path: '../.env'})

const port = 3001;

const { createApp } = require('@unleash/proxy');

const app = createApp({
    unleashUrl: process.env.UNLEASH_URL,
    unleashApiToken: process.env.UNLEASH_API_TOKEN,
    proxySecrets: ['secret-squirrel', 'shhhh'],
    refreshInterval: 1000,
});

app.listen(port, () =>
    // eslint-disable-next-line no-console
    console.log(`Unleash Proxy listening on http://localhost:${port}/proxy`),
);