<template>
    <form
        class="max-w-xl"
        method="POST"
        action="/register"
        @submit.prevent="onSubmit"
        @keydown="form.errors.clear($event.target.name)"
    >
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full px-3">
                <label class="block uppercase tracking-wide text-gray-700 font-bold mb-2"
                       :class="{'text-red-500' : form.errors.has('name')}"
                       for="grid-name">
                    Name
                </label>
                <input
                    class="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
                    :class="{'border border-red-500' : form.errors.has('name')}"
                    id="grid-name"
                    type="text"
                    placeholder="Jane"
                    v-model="form.name"
                >
                <p class="text-gray-600 italic">This is how we'll publicly display your name</p>

                <p
                    v-if="form.errors.has('name')"
                    class="text-red-500 text-xs italic mt-2"
                    v-text="form.errors.get('name')"
                />
            </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full px-3">
                <label class="block uppercase tracking-wide text-gray-700 font-bold mb-2"
                       :class="{'text-red-500' : form.errors.has('email')}"
                       for="grid-email">
                    Email
                </label>
                <input
                    class="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
                    :class="{'border border-red-500' : form.errors.has('email')}"
                    id="grid-email"
                    type="email"
                    placeholder="your@email.com"
                    v-model="form.email"
                >

                <p
                    v-if="form.errors.has('email')"
                    class="text-red-500 text-xs italic mt-2"
                    v-text="form.errors.get('email')"
                />
            </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 font-bold mb-2"
                       :class="{'text-red-500' : form.errors.has('password')}"
                       for="grid-password">
                    Password
                </label>
                <input
                    class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    :class="{'border border-red-500' : form.errors.has('password')}"
                    id="grid-password"
                    type="password"
                    placeholder="Password"
                    v-model="form.password"
                >

                <p
                    v-if="form.errors.has('password')"
                    class="text-red-500 text-xs italic mt-2"
                    v-text="form.errors.get('password')"
                />
            </div>
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label class="block uppercase tracking-wide text-gray-700 font-bold mb-2"
                       for="grid-password-confirmation">
                    Confirm
                </label>
                <input
                    class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="grid-password-confirmation"
                    type="password"
                    placeholder="Confirm Password"
                    v-model="form.password_confirmation"
                >
            </div>
        </div>
        <div class="flex flex-wrap">
            <button
                class="bg-blue-900 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                :disabled="form.errors.any() || submitting"
            >
                Sign Up
            </button>
        </div>
    </form>
</template>

<script>
    import Form from '../modules/Form.js'
    import MixinCsrf from "./MixinCsrf";

    export default {
        name: 'UserRegister',
        mixins: [MixinCsrf],
        data() {
            return {
                submitting: false,
                form: new Form({
                    name: '',
                    email: '',
                    password: '',
                    password_confirmation: ''
                })
            }
        },
        methods: {
            onSubmit() {
                this.submitting = true
                this.form.post('/register')
                    .then((response) => {
                        flash('Signing you up...')

                        setTimeout(() => {
                            window.location.replace('/')
                        }, 500)

                        this.submitting = false
                    })
                    .catch((errors) => {
                        flash('User registration failed.', 'danger')
                        this.submitting = false
                    })
            }
        }
    }
</script>
