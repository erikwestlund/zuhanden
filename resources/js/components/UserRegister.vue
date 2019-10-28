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
                <label
                    class="block uppercase tracking-wide text-gray-700 font-bold mb-2"
                    :class="{'text-red-500' : form.errors.has('name')}"
                    for="grid-name"
                >
                    Name
                </label>
                <input
                    id="grid-name"
                    v-model="form.name"
                    class="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
                    :class="{'border border-red-500' : form.errors.has('name')}"
                    type="text"
                    placeholder="Your Name"
                >
                <p class="text-gray-600 italic">
                    This is how we'll publicly display your name
                </p>

                <p
                    v-if="form.errors.has('name')"
                    class="text-red-500 text-xs italic mt-2"
                    v-text="form.errors.get('name')"
                />
            </div>
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full px-3">
                <label
                    class="block uppercase tracking-wide text-gray-700 font-bold mb-2"
                    :class="{'text-red-500' : form.errors.has('email')}"
                    for="grid-email"
                >
                    Email
                </label>
                <input
                    id="grid-email"
                    v-model="form.email"
                    class="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
                    :class="{'border border-red-500' : form.errors.has('email')}"
                    type="email"
                    placeholder="your@email.com"
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
                <label
                    class="block uppercase tracking-wide text-gray-700 font-bold mb-2"
                    :class="{'text-red-500' : form.errors.has('password')}"
                    for="grid-password"
                >
                    Password
                </label>
                <input
                    id="grid-password"
                    v-model="form.password"
                    class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    :class="{'border border-red-500' : form.errors.has('password')}"
                    type="password"
                    placeholder="Password"
                >

                <p
                    v-if="form.errors.has('password')"
                    class="text-red-500 text-xs italic mt-2"
                    v-text="form.errors.get('password')"
                />
            </div>
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
                <label
                    class="block uppercase tracking-wide text-gray-700 font-bold mb-2"
                    for="grid-password-confirmation"
                >
                    Confirm
                </label>
                <input
                    id="grid-password-confirmation"
                    v-model="form.password_confirmation"
                    class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    type="password"
                    placeholder="Confirm Password"
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

export default {
    name: 'UserRegister',

    data () {
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
        onSubmit () {
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
