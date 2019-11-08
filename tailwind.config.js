module.exports = {
    theme: {
        fontFamily: {
            sans: [
                'Source Sans Pro',
                '-apple-system',
                'BlinkMacSystemFont',
                '"Segoe UI"',
                'Roboto',
                '"Helvetica Neue"',
                'Arial',
                '"Noto Sans"',
                'sans-serif',
                '"Apple Color Emoji"',
                '"Segoe UI Emoji"',
                '"Segoe UI Symbol"',
                '"Noto Color Emoji"',
            ],
            'serif': ['Merriweather', 'Georgia', 'Cambria', 'Times New Roman', 'Times', 'serif']
        },
        screens: {
            'sm': '576px',
            // => @media (min-width: 576px) { ... }

            'md': '768px',
            // => @media (min-width: 768px) { ... }

            'lg': '992px',
            // => @media (min-width: 992px) { ... }

            'xl': '1200px',
            // => @media (min-width: 1200px) { ... }
        },
        extend: {}
    },
    variants: {},
    plugins: []
}
