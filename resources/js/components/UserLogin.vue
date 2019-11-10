<template>
    <form
        class="w-full max-w-md"
        method="POST"
        action="/login"
        @submit.prevent="onSubmit"
        @keydown="form.errors.clear($event.target.name)"
    >
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
            <div class="w-full px-3">
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
        </div>
        <div class="flex flex-wrap">
            <button
                class="bg-blue-900 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                :disabled="form.errors.any() || submitting"
            >
                Sign In
            </button>
        </div>
    </form>
</template>x

<script>
    import Form from '../modules/Form.js'
    import MixinSubmitting from './MixinSubmitting'

    export default {
        mixins: [MixinSubmitting],

        data () {
            return {
                submittingType: 'logging_in',
                showLoginModal: false,
                form: new Form({
                    next: this.next,
                    email: '',
                    password: ''
                })
            }
        },

        methods: {
            onSubmit () {
                this.turnOnSubmitting()
                this.form.post('/login')
                    .then((response) => {
                        Event.fire('closeLoginModal')

                        flash('Logging you in...')

                        setTimeout(() => {
                            location.reload()
                        }, 500)

                        this.turnOffSubmitting()
                    })
                    .catch(errors => {
                        this.turnOffSubmitting()
                    })
            }
        }
    }
</script>
