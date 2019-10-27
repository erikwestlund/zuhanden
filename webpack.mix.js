let mix = require('laravel-mix');
let tailwindcss = require('tailwindcss');
let glob = require("glob-all");
let PurgecssPlugin = require("purgecss-webpack-plugin");

// Custom PurgeCSS extractor for Tailwind that allows special characters in
// class names.
//
// https://github.com/FullHuman/purgecss#extractor
class TailwindExtractor {
    static extract(content) {
        return content.match(/[A-Za-z0-9-_:\/]+/g) || [];
    }
}

mix.setPublicPath('storage/static')
    .setResourceRoot('/resources')
    .sass('resources/sass/app.scss', 'storage/static/css/app.css')
    .js('resources/js/app.js', 'storage/static/js/app.js')
    .options({
        processCssUrls: false,
        postCss: [tailwindcss('./tailwind.config.js')],
    })
    .extract([
        'vue',
        'axios',
        'lodash'
    ])
    .version();

if (mix.inProduction()) {
    const whitelistPatterns = [
        /^alert/,
        /^trx-/,
        /^component-*/,
        /^fa-/,
    ];

    mix.webpackConfig({
        plugins: [
            new PurgecssPlugin({

                // Specify the locations of any files you want to scan for class names.
                paths: glob.sync([
                    path.join(__dirname, "**/*.html"),
                    path.join(__dirname, "resources/js/**/*.vue")
                ]),
                whitelistPatterns: whitelistPatterns,
                extractors: [
                    {
                        extractor: TailwindExtractor,

                        // Specify the file extensions to include when scanning for
                        // class names.
                        extensions: ["html", "js", "py", "vue"]
                    }
                ]
            })
        ]
    });
}
