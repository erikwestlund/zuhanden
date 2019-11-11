<template>
    <div>
        <header>
            <nav>
                <div class="container mx-auto flex items-center justify-between flex-wrap py-3 px-3 md:px-0">
                    <div class="flex items-center flex-shrink-0 text-white mr-12">
                        <span class="font-semibold font-serif text-4xl">
                            <fa-icon
                                class="mr-4 text-blue-400"
                                :icon="['fad', 'university']"
                            />
                            <a
                                href="/"
                                class="hover:text-blue-100"
                            >Academic</a>
                        </span>
                    </div>
                    <div
                        class="w-full flex-grow md:flex md:items-center md:w-auto"
                    />
                    <div class="md:flex items-center">
                        <inertia-link
                            v-if="signedOut"
                            href="/users/sign-in"
                            class="btn-outline"
                        >
                            <fa-icon
                                class="mr-2"
                                :icon="['fad', 'sign-in']"
                            />
                            Sign In
                        </inertia-link>
                        <inertia-link
                            v-if="signedIn"
                            href="/users/sign-out"
                            class="btn-outline"
                        >
                            <fa-icon
                                class="mr-2"
                                :icon="['fad', 'sign-out']"
                            />
                            Sign Out
                        </inertia-link>
                    </div>
                </div>
            </nav>
        </header>
        <main
            role="main"
            class="sans-serif container mx-auto text-white p-4"
        >
            <flash-messages class="mb-4" />
            <article>
                <slot />
            </article>
        </main>
    </div>
</template>

<script>
    import FlashMessages from '@/Shared/FlashMessages'

    export default {
        components: {
            FlashMessages
        },
        props: {
            title: {
                type: String,
                default: 'Academic.page'
            }
        },
        computed: {
            signedIn () {
                return Boolean(this.$page.auth.user)
            },
            signedOut () {
                return !this.signedIn
            }
        },
        watch: {
            title: {
                immediate: true,
                handler (title) {
                    document.title = title
                }
            }
        }
    }
</script>
