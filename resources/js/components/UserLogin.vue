<template>
    <div class="flex mt-8">
        <form
            class="w-full max-w-md"
            method="POST"
            action="/login"
            @submit.prevent="onSubmit"
            @keydown="form.errors.clear($event.target.name)"
        >
            <div class="flex flex-wrap -mx-3 mb-3">
                <div class="w-full px-3">
                    <label
                        class="text-input-label"
                        :class="{'text-red' : form.errors.has('email')}"
                        for="grid-email"
                    >
                        Email Address
                    </label>
                    <input
                        id="grid-email"
                        v-model="form.email"
                        class="text-input focus:outline-none focus:border-grey"
                        :class="{'border border-red' : form.errors.has('email')}"
                        name="email"
                        placeholder="Email Address"
                    >
                    <p
                        v-if="form.errors.has('email')"
                        class="text-red text-xs italic"
                        v-text="form.errors.get('email')"
                    />
                </div>
            </div>

            <div class="flex flex-wrap -mx-3 mb-3">
                <div class="w-full px-3">
                    <label
                        class="text-input-label"
                        :class="{'text-red' : form.errors.has('password')}"
                        for="grid-password"
                    >
                        Password
                    </label>
                    <input
                        id="grid-password"
                        v-model="form.password"
                        type="password"
                        class="text-input focus:outline-none focus:border-grey"
                        :class="{'border border-red' : form.errors.has('password')}"
                        name="password"
                        placeholder="Password"
                    >
                    <p
                        v-if="form.errors.has('password')"
                        class="text-red text-xs italic"
                        v-text="form.errors.get('password')"
                    />
                </div>
            </div>

            <div class="flex flex-wrap mb-6">
                <label class="text-grey-dark">
                    <input
                        class="mr-2 leading-tight"
                        type="checkbox"
                    >
                    <span class="cursor-pointer">
                        Remember Me
                    </span>
                </label>
            </div>
            <div class="flex flex-wrap mb-3">
                <button
                    class="btn btn-blue hover:bg-blue-darkest hover:border-blue-darkest"
                    :disabled="form.errors.any() || logging_in"
                >
                    <span v-if="! logging_in">
                        <fa-icon
                            class="mr-2"
                            :icon="['far', 'sign-in']"
                        />
                        Log In
                    </span>
                    <submitting-label
                        v-if="logging_in"
                        type="logging_in"
                    />
                </button>
            </div>
        </form>
    </div>
</template>x

<script>
import Form from '../modules/Form.js'
import MixinSubmitting from './MixinSubmitting'

export default {
    mixins: [MixinSubmitting],

    props: {
        next: {
            type: String,
            default: null
        }
    },

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
                        window.location.replace(response.next)
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
