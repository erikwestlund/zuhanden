<template>
    <layout title="Login to Academic">
        <h1 class="text-center font-bold text-3xl">Welcome Back!</h1>
        <form class="mt-8 mx-auto max-w-md bg-white rounded-lg shadow-lg overflow-hidden" @submit.prevent="submit">
            <div class="px-10 py-12">
                <text-input v-model="form.email" :errors="$page.errors.email" label="Email" type="email"
                            autofocus autocapitalize="off"/>
                <text-input v-model="form.password" :errors="$page.errors.password" class="mt-6" label="Password" type="password"/>
            </div>
            <div class="px-10 py-4 bg-grey-lightest border-t border-grey-lighter flex justify-between items-center">
                <a class="hover:underline" tabindex="-1" href="#reset-password">Forget password?</a>
                <loading-button :loading="sending" class="btn-indigo" type="submit">Login</loading-button>
            </div>
        </form>
    </layout>
</template>

<script>
    import Layout from '@/Shared/Layout'
    import LoadingButton from '@/Shared/LoadingButton'
    import TextInput from '@/Shared/TextInput'

    export default {
        components: {
            Layout,
            LoadingButton,
            TextInput
        },
        props: {
            errors: Object
        },
        data () {
            return {
                sending: false,
                form: {
                    email: null,
                    password: null
                }
            }
        },
        methods: {
            submit () {
                this.sending = true
                this.$inertia.post('/login', {
                    email: this.form.email,
                    password: this.form.password,
                }).then(() => this.sending = false)
            },
        },
    }
</script>

<style scoped>

</style>
