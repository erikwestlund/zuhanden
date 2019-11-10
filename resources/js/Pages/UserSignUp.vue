<template>
    <layout title="Sign Up With Academic">
        <h1 class="text-center font-bold text-3xl">
            Get Signed Up
        </h1>
        <form
            class="mt-8 mx-auto max-w-md bg-white rounded-lg shadow-lg overflow-hidden"
            @submit.prevent="submit"
        >
            <div class="px-10 py-12">
                <text-input
                    v-model="form.name"
                    :errors="$page.errors.name"
                    label="Name"
                    type="name"
                    placeholder="Your Name"
                    autofocus
                    autocapitalize="off"
                />
                <text-input
                    v-model="form.email"
                    :errors="$page.errors.email"
                    class="mt-6"
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
                <text-input
                    v-model="form.password_confirmation"
                    :errors="$page.errors.password_confirmation"
                    class="mt-6"
                    label="Confirm"
                    type="password"
                />
                <loading-button
                    :loading="submitting"
                    class="mt-8 w-full btn btn-orange"
                    type="submit"
                >
                    Sign Up
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
                default: () => {}
            }
        },
        data () {
            return {
                submitting: false,
                form: {
                    name: '',
                    email: '',
                    password: '',
                    password_confirmation: ''
                }
            }
        },
        methods: {
            submit () {
                this.submitting = true
                this.$inertia.post('/users/sign-up', this.form).then(() => {
                    this.submitting = false
                })
            }
        }
    }
</script>

<style scoped>

</style>
