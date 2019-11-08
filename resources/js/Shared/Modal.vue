<template>
    <transition name="modal">
        <div
            v-show="show"
            class="modal-mask"
            @click="$emit('close')"
        >
            <div class="modal-wrapper">
                <div
                    class="modal-container bg-white my-8 mx-auto p-6 rounded-lg shadow-lg"
                    :class="{'lg': large, 'sm':small}"
                    @click.stop
                >
                    <div class="modal-header">
                        <slot name="header">
                            default header
                        </slot>
                    </div>

                    <div class="modal-body mt-6 mb-2">
                        <slot name="body">
                            default body
                        </slot>
                    </div>

                    <div
                        v-show="! noFooter"
                        class="modal-footer mt-10 flex content-end flex-wrap"
                    >
                        <div class="w-3/4 m-auto text-sm">
                            <slot name="footer" />
                        </div>
                        <div class="w-1/4 text-right">
                            <button
                                class="btn btn-gray hover:bg-gray hover:border-gray"
                                @click="$emit('close')"
                            >
                                <fa-icon
                                    class="mr-2"
                                    :icon="['far', 'times']"
                                />
                                {{ doneText }}
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </transition>
</template>

<script>
export default {
    name: 'Modal',
    props: {
        doneText: {
            type: String,
            default: 'OK'
        },
        noFooter: {
            type: Boolean,
            default: false
        },
        doneIcon: {
            type: String,
            default: 'times'
        },
        large: {
            type: Boolean,
            default: false
        },
        small: {
            type: Boolean,
            default: false
        },
        show: {
            type: Boolean,
            default: false
        }
    },

    created () {
        document.addEventListener('keyup', this.escapeKeyListener)
    },

    destroyed () {
        document.removeEventListener('keyup', this.escapeKeyListener)
    },

    methods: {
        escapeKeyListener (event) {
            if (event.keyCode === 27) {
                this.$emit('close')
            }
        }
    }
}
</script>

<style scoped>
    .modal-mask {
        position: fixed;
        z-index: 9998;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .5);
        display: table;
        transition: opacity .3s ease;
    }

    .modal-wrapper {
        display: table-cell;
        vertical-align: middle;
    }

    .modal-container {
        width: 500px;
        transition: all .3s ease;
    }

    .modal-container.lg {
        width: 90%;
    }

    .modal-container.sm {
        width: 350px;
    }

    .modal-header h3 {
        margin-top: 0;
        color: #42b983;
    }

    .modal-enter {
        opacity: 0;
    }

    .modal-leave-active {
        opacity: 0;
    }

    .modal-enter .modal-container,
    .modal-leave-active .modal-container {
        -webkit-transform: scale(1.1);
        transform: scale(1.1);
    }
</style>
