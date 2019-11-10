<template>
    <layout title="Sign In To Academic">
        <h1 class="text-center font-bold text-3xl">
            Welcome Back!
        </h1>
        <form
            class="mt-8 mx-auto max-w-md bg-white rounded-lg shadow-lg overflow-hidden"
            @submit.prevent="submit"
        >
            <div class="px-10 py-12">
                <text-input
                    v-model="form.email"
                    :errors="$page.errors.email"
                    label="Email"
                    type="email"
                    autofocus
                    autocapitalize="off"
                />
                <text-input
                    v-model="form.password"
                    :errors="$page.errors.password"
                    class="mt-6"
                    label="Password"
                    type="password"
                />
            </div>
            <div class="px-10 py-4 bg-gray-100 border-t border-gray-300 flex justify-between items-center">
                <a
                    class="hover:underline"
                    tabindex="-1"
                    href="#reset-password"
                >Forget password?</a>
                <loading-button
                    :loading="submitting"
                    class="btn btn-orange"
                    type="submit"
                >
                    Sign In
                </loading-button>
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
            errors: {
                type: Object,
                default: () => {
                }
            }
        },
        data () {
            return {
                submitting: false,
                form: {
                    email: '',
                    password: ''
                }
            }
        },
        methods: {
            submit () {
                this.submitting = true
                this.$inertia.post('/users/sign-in', this.form)
                    .then(() => {
                        this.submitting = false
                    })
            }
        }
    }
</script>

<style scoped>

</style>
