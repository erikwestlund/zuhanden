export default class {
    constructor () {
        this.vue = new Vue()
    }

    fire (event, data = null) {
        this.vue.$emit(event, data)
    }

    listen (event, callback) {
        this.vue.$on(event, callback)
    }
}
