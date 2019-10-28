<template>
    <transition name="trx-fade">
        <div
            v-show="show"
            class="alert alert-flash"
            :class="'alert-'+level"
            role="alert"
        >
            {{ message }}
        </div>
    </transition>
</template>

<script>
export default {
    name: 'Flash',

    props: {
        initialMessage: {
            required: true,
            type: String,
            default: ''
        },
        initialLevel: {
            default: 'success',
            type: String
        },
        initialDuration: {
            default: 3,
            type: Number
        }
    },

    data () {
        return {
            message: this.initialMessage,
            level: this.initialLevel,
            duration: this.initialDuration,
            show: false
        }
    },

    created () {
        Event.listen('flash', data => this.flash(data))
    },

    mounted () {
        this.$nextTick(function () {
            if (this.initialMessage) {
                this.flash({
                    message: this.initialMessage,
                    level: this.initialLevel,
                    duration: this.initialDuration
                })
            }
        })
    },

    methods: {
        flash (data) {
            this.message = data.message || this.message
            this.level = data.level || this.level
            const duration = data.duration || this.duration
            this.show = true

            this.hide(duration)
        },

        hide (duration) {
            setTimeout(() => {
                this.show = false
            }, duration * 1000)
        }
    }
}
</script>

<style scoped>
    .alert-flash {
        position: fixed;
        right: 25px;
        bottom: 25px;
    }
</style>
