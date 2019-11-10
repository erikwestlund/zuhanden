<template>
    <transition name="fade">
        <div
            v-if="show"
            class="flex items-center"
            :class="style"
            role="alert"
        >
            <fa-icon
                class="mr-4"
                :icon="['fad', icon]"
            />
            <p class="flex-grow">
                {{ message }}
            </p>

            <fa-icon
                class="ml-2 cursor-pointer"
                :icon="['far', 'times']"
                @click="$emit('close', true)"
            />
        </div>
    </transition>
</template>

<script>
    export default {
        props: {
            show: Boolean,
            type: {
                type: String,
                default: 'info'
            },
            message: {
                type: String,
                default: ''
            }
        },
        data () {
            return {
                icons: {
                    success: 'check-circle',
                    error: 'bomb',
                    danger: 'exclamation-circle',
                    warning: 'exclamation-circle',
                    info: 'info-circle'
                }
            }
        },
        computed: {
            style () {
                return `alert-${this.type}`
            },
            icon () {
                return this.icons[this.type]
            }
        }
    }
</script>
