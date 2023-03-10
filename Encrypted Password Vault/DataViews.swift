//
//  DataViews.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/22/23.
//

import SwiftUI

struct DataViews: View {
    @Binding var showPathViews: Bool
    @Binding var showPasswordViews: Bool
    @Binding var showDataViews: Bool
    
    @State var password = getPassword()
    @State var path = getPath()
    
    var body: some View {
        VStack {
            Text("Data Location: " + (getPath() ?? "~/Documents"))
            
            let data = runRead(path: path ?? "~/Downloads", password: password ?? "")
            Grid() {
                ForEach((0...data.count), id: \.self) { i in
                    GridRow {
                        Text(data[i].getKey())
                        Text(data[i].getUser())
                        Text(data[i].getPass())
                    }
                }
            }
            
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

struct DataViews_Previews: PreviewProvider {
    static var previews: some View {
        DataViews(showPathViews: TestValues.$testFalse, showPasswordViews: TestValues.$testFalse, showDataViews: TestValues.$testTrue)
    }
}
