import {EquipmentResource} from './resources'

export default {
    getEquipmentList: function() {
        return EquipmentResource.get()
    }
}
