<template>
    <nav class="flex items-center justify-between flex-wrap bg-blue-900 py-3 px-3 md:px-12 shadow-lg">
        <div class="flex items-center flex-shrink-0 text-white mr-12">
            <span class="font-semibold text-4xl">
                <fa-icon
                    class="mr-1 text-blue-400"
                    :icon="['fas', 'hammer']"
                /> Zuhanden
            </span>
        </div>
        <div class="block md:hidden">
            <button
                class="flex items-center px-3 py-2 border rounded text-blue-900 bg-white border-white hover:text-blue-700 hover:border-white"
                @click="toggleMobileNav()"
            >
                <fa-icon :icon="['far', 'bars']"/>
            </button>
        </div>
        <div
            class="w-full flex-grow md:flex md:items-center md:w-auto"
            :class="{'block': showMobileNav, 'hidden' : ! showMobileNav}"
        >
            <div class="text-lg md:flex-grow">
                <a
                    href="#responsive-header"
                    class="block mt-4 md:inline-block md:mt-0 text-blue-100 hover:text-blue-200 mr-4"
                >
                    About
                </a>
                <a
                    href="#responsive-header"
                    class="block mt-4 md:inline-block md:mt-0 text-blue-100 hover:text-blue-200"
                >
                    Blog
                </a>
            </div>
            <div class="md:flex items-center" v-if="showUserActions">
                <a
                    v-if="! loggedIn"
                    href="/register"
                    class="block md:inline-block text-lg md:px-4 py-2 leading-none md:border md:rounded text-white border-white md:hover:border-transparent md:hover:text-blue-900 md:hover:bg-white mt-4 md:mt-0 md:mr-2"
                >
                    <fa-icon
                        class="mr-2"
                        :icon="['fas', 'user-plus']"
                    />
                    Sign Up
                </a>
                <a
                    v-if="! loggedIn"
                    href="/login"
                    @click.prevent
                    @click.exact="showLoginModal = true"
                    class="block md:inline-block text-lg md:px-4 py-2 leading-none md:border md:rounded text-white border-white md:hover:border-transparent md:hover:text-blue-900 md:hover:bg-white mt-4 md:mt-0"
                >
                    <fa-icon
                        class="mr-2"
                        :icon="['fas', 'sign-in']"
                    />
                    Sign In
                </a>
                <span class="text-white mr-8" v-if="loggedIn">
                    <fa-icon class="mr-1" :icon="['fas', 'user-circle']"/>

                    <span v-if="userName">
                        {{ user.name }}
                    </span>
                </span>
                <a
                    v-if="loggedIn"
                    href="/logout"
                    class="block md:inline-block text-lg md:px-4 py-2 leading-none md:border md:rounded text-white border-white md:hover:border-transparent md:hover:text-blue-900 md:hover:bg-white mt-4 md:mt-0"
                >
                    <fa-icon
                        class="mr-2"
                        :icon="['fas', 'sign-out']"
                    />
                    Sign Out
                </a>
            </div>
        </div>
        <modal
            v-if="showUserActions"
            small
            :show="showLoginModal"
            done-text="Close"
            @close="showLoginModal = false"
        >
            <h3 slot="header" class="text-2xl text-blue-900">
                <fa-icon
                    class="mr-2"
                    :icon="['far', 'sign-in']"
                />
                Sign In
            </h3>

            <div slot="body">
                <user-login/>
            </div>

            <div slot="footer">
                <fa-icon
                    class="mr-2 text-grey-dark"
                    :icon="['far', 'key']"
                />
                <a
                    class="text-blue-900 hover:text-blue-700  pt-4"
                    href="/users/reset-password"
                >
                    Reset
                    Password
                </a>
            </div>
        </modal>
    </nav>
</template>

<script>
    import Modal from './Modal'
    import UserLogin from './UserLogin'

    export default {
        name: 'NavigationBar',

        props: {
            showUserActions: {
                default: true,
                type: Boolean
            }
        },

        components: {
            Modal,
            UserLogin
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
                return this.state.user.loggedIn
            },

            user() {
                return this.state.user
            },

            userName() {
                return this.state.user.name || ''
            }

        },

        created() {
            Event.listen('closeLoginModal', () => {
                this.showLoginModal = false
            })

            Event.listen('userLoggedIn', () => {
                this.state.user.loggedIn = true
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
