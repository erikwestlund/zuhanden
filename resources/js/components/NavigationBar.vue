<template>
    <nav class="flex items-center justify-between flex-wrap bg-blue-500 py-3 px-3 md:px-6">
        <div class="flex items-center flex-shrink-0 text-white mr-12">
            <span class="font-semibold text-4xl">Zuhandens</span>
        </div>
        <div class="block lg:hidden">
            <button
                class="flex items-center px-3 py-2 border rounded text-blue-200 border-blue-400 hover:text-white hover:border-white">
                Test
            </button>
        </div>
        <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
            <div class="text-lg lg:flex-grow">
                <a href="#responsive-header"
                   class="block mt-4 lg:inline-block lg:mt-0 text-blue-200 hover:text-white mr-4">
                    About
                </a>
                <a href="#responsive-header" class="block mt-4 lg:inline-block lg:mt-0 text-blue-200 hover:text-white">
                    Blog
                </a>
            </div>
            <div>
                <a href="#"
                   class="inline-block text-lg px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-blue-500 hover:bg-white mt-4 lg:mt-0">Register</a>
            </div>
        </div>
    </nav>
</template>

<script>
    import Modal from './Modal'

    export default {
        name: 'NavigationBar',
        components: {
            Modal
        },
        data() {
            return {
                state: State,
                showLoginModal: false,
                showMobileNav: false
            }
        },
        computed: {
            loggedIn() {
                return this.state.user.logged_in
            },

        },
        created() {
            Event.listen('closeLoginModal', () => {
                this.showLoginModal = false
            })
        },
        methods: {
            toggleMobileNav() {
                this.showMobileNav = !this.showMobileNav
            }
        }
    }
</script>

<style scoped>

</style>
