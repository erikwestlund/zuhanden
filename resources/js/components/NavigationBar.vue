<template>
    <nav class="flex items-center justify-between flex-wrap bg-blue-900 py-3 px-3 md:px-12">
        <div class="flex items-center flex-shrink-0 text-white mr-12">
            <span class="font-semibold text-4xl">
                <fa-icon class="mr-1" :icon="['fas', 'hammer']"></fa-icon> Zuhanden
            </span>
        </div>
        <div class="block md:hidden">
            <button
                class="flex items-center px-3 py-2 border rounded text-blue-900 bg-white border-white hover:text-blue-700 hover:border-white"
                @click="toggleMobileNav()"
            >
                <fa-icon :icon="['far', 'bars']"></fa-icon>
            </button>
        </div>
        <div class="w-full flex-grow md:flex md:items-center md:w-auto" :class="{'block': showMobileNav, 'hidden' : ! showMobileNav}">
            <div class="text-lg md:flex-grow">
                <a href="#responsive-header"
                   class="block mt-4 md:inline-block md:mt-0 text-blue-100 hover:text-blue-200 mr-4">
                    About
                </a>
                <a href="#responsive-header" class="block mt-4 md:inline-block md:mt-0 text-blue-100 hover:text-blue-200">
                    Blog
                </a>
            </div>
            <div class="md:flex">
                <a href="/register"
                   v-if="! loggedIn"
                   class="block md:inline-block text-lg md:px-4 py-2 leading-none md:border md:rounded text-white border-white md:hover:border-transparent md:hover:text-blue-900 md:hover:bg-white mt-4 md:mt-0 md:mr-2">
                    <fa-icon class="mr-2" :icon="['fas', 'user-plus']"></fa-icon>
                    Sign Up
                </a>
                <a href="/register"
                   v-if="! loggedIn"
                   class="block md:inline-block text-lg md:px-4 py-2 leading-none md:border md:rounded text-white border-white md:hover:border-transparent md:hover:text-blue-900 md:hover:bg-white mt-4 md:mt-0">
                    <fa-icon class="mr-2" :icon="['fas', 'sign-in']"></fa-icon>
                    Log In
                </a>
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

        computed: {
          loggedIn() {
              return this.state.user.loggedIn
          }
        },

        data() {
            return {
                state: State,
                showLoginModal: false,
                showMobileNav: false
            }
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
