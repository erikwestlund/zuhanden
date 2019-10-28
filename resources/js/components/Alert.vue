<template>
    <div>
        <transition name="trx-fade">
            <div
                v-show="show"
                role="alert"
                class="alert mb-4"
                :class="'alert-' + category"
            >
                <button
                    v-if="!important"
                    type="button"
                    class="float-right"
                    @click="hide()"
                >
                    <fa-icon
                        :class="'alert-x-' + category"
                        :icon="['far', 'times']"
                    />
                </button>

                <slot />
            </div>
        </transition>
    </div>
</template>

<script>
export default {
    name: 'Alert',

    props: {
        category: {
            type: String,
            default: 'message'
        },
        duration: {
            type: Number,
            default: 3000
        },
        important: {
            type: Boolean,
            default: false
        },
        initShow: {
            type: Boolean,
            default: true
        },
        temporary: {
            type: Boolean,
            default: true
        }
    },

    data () {
        return {
            show: this.initShow
        }
    },

    created () {
        Event.listen('hideAlert', () => this.hide())
    },

    mounted () {
        this.$nextTick(() => {
            if (this.temporary) {
                setTimeout(() => {
                    Event.fire('hideAlert')
                },
                this.duration)
            }
        })
    },

    methods: {
        hide () {
            this.show = false
        }
    }
}
</script>

<style scoped>
</style>
