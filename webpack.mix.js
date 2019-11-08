const cssImport = require('postcss-import')
const cssNesting = require('postcss-nesting')
const mix = require('laravel-mix');
const path = require('path')
const tailwindcss = require('tailwindcss');
const glob = require("glob-all");
const PurgecssPlugin = require("purgecss-webpack-plugin");


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
    // .sass('resources/sass/app.scss', 'storage/static/css/app.css')
    // .js('resources/js/old.js', 'storage/static/js/old.js')
    .postCss('resources/css/app.css', 'storage/static/css/app.css', [
        cssImport(),
        cssNesting(),
        require('tailwindcss'),
    ])
    .js('resources/js/app.js', 'storage/static/js/app.js')
    .options({
        postCss: [tailwindcss('./tailwind.config.js')],
    })
    .extract([
        // 'vue',
        'axios',
        'lodash'
    ])
    .webpackConfig({
        output: {chunkFilename: '[name].js?id=[chunkhash]'},
        resolve: {
            alias: {
                'vue$': 'vue/dist/vue.runtime.esm.js',
                '@': path.resolve('resources/js'),
            },
        },
    })
    .babelConfig({
        plugins: ['@babel/plugin-syntax-dynamic-import'],
    })
    .version()
    .sourceMaps()

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
