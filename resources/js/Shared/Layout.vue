<template>
    <div>
        <header>
            <nav class="flex items-center justify-between flex-wrap bg-blue-900 py-3 px-3 md:px-12 shadow-lg">
                <div class="flex items-center flex-shrink-0 text-white mr-12">
                    <span class="font-semibold font-serif text-4xl">
                        <fa-icon
                            class="mr-4 text-blue-400"
                            :icon="['fad', 'university']"
                        />
                        <a href="/" class="text-blue-100 hover:text-blue-100">Academic</a>
                    </span>
                </div>
                <div
                    class="w-full flex-grow md:flex md:items-center md:w-auto"
                >
                </div>
                <div class="md:flex items-center">
                    <inertia-link
                        href="/login"
                        class="btn-outline"
                    >
                        <fa-icon
                            class="mr-2"
                            :icon="['fad', 'sign-in']"
                        />
                        Sign In
                    </inertia-link>
                    <inertia-link
                        href="/register"
                        class="btn-outline"
                    >
                        <fa-icon
                            class="mr-2"
                            :icon="['fad', 'user-plus']"
                        />
                        Sign Up
                    </inertia-link>
                </div>
            </nav>
        </header>
        <main role="main" class="sans-serif container mx-auto pt-12">
            <article>
                <slot/>
            </article>
        </main>
    </div>
</template>

<script>
    export default {
        props: {
            title: String,
        },
        watch: {
            title: {
                immediate: true,
                handler(title) {
                    document.title = title
                },
            },
        },
    }
</script>
