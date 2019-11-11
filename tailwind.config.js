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
        fontSize: {
            'xs': '.75rem',
            'sm': '.875rem',
            'tiny': '.875rem',
            'base': '1rem',
            'lg': '1.125rem',
            'xl': '1.25rem',
            '2xl': '1.5rem',
            '3xl': '1.875rem',
            '4xl': '2.25rem',
            '5xl': '3rem',
            '6xl': '4rem',
            '15xl': '15rem',
            '20xl': '20rem',
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
